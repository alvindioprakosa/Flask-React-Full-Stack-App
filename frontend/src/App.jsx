import { useState, useEffect } from "react";
import ContactList from "./ContactList";
import ContactForm from "./ContactForm";
import "./App.css";

function App() {
  const [contacts, setContacts] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [currentContact, setCurrentContact] = useState({});
  const [loading, setLoading] = useState(false);

  // Fetch contacts when the component mounts
  useEffect(() => {
    fetchContacts();
  }, []);

  const fetchContacts = async () => {
    setLoading(true);
    try {
      const response = await fetch("http://127.0.0.1:5000/contacts");
      const data = await response.json();
      setContacts(data.contacts);
    } catch (error) {
      alert("Failed to fetch contacts");
    } finally {
      setLoading(false);
    }
  };

  // Close modal
  const closeModal = () => {
    setIsModalOpen(false);
    setCurrentContact({});
  };

  // Open Create Modal
  const openCreateModal = () => {
    if (!isModalOpen) setIsModalOpen(true);
  };

  // Open Edit Modal
  const openEditModal = (contact) => {
    if (isModalOpen) return;
    setCurrentContact(contact);
    setIsModalOpen(true);
  };

  // Callback after creating or updating a contact
  const onUpdate = () => {
    closeModal();
    fetchContacts();
  };

  return (
    <>
      <ContactList
        contacts={contacts}
        updateContact={openEditModal}
        updateCallback={onUpdate}
      />
      <button onClick={openCreateModal} disabled={isModalOpen || loading}>
        Create New Contact
      </button>
      {isModalOpen && (
        <div className="modal">
          <div className="modal-content">
            <span className="close" onClick={closeModal}>
              &times;
            </span>
            <ContactForm
              existingContact={currentContact}
              updateCallback={onUpdate}
            />
          </div>
        </div>
      )}
    </>
  );
}

export default App;
