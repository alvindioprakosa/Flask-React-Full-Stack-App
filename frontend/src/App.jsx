import { useState, useEffect } from "react";
import ContactList from "./ContactList";
import ContactForm from "./ContactForm";
import "./App.css";

function App() {
  const [contacts, setContacts] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [currentContact, setCurrentContact] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    fetchContacts();
  }, []);

  const fetchContacts = async () => {
    setLoading(true);
    try {
      const response = await fetch("http://127.0.0.1:5000/contacts");
      const data = await response.json();
      setContacts(data.contacts || []);
      setError("");
    } catch (err) {
      setError("Failed to fetch contacts.");
    } finally {
      setLoading(false);
    }
  };

  const openModal = (contact = null) => {
    if (isModalOpen) return;
    setCurrentContact(contact);
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
    setCurrentContact(null);
  };

  const onUpdate = () => {
    closeModal();
    fetchContacts();
  };

  return (
    <>
      <h1>Contact Manager</h1>
      {error && <p className="error">{error}</p>}
      {loading ? <p>Loading contacts...</p> : (
        <ContactList
          contacts={contacts}
          updateContact={openModal}
          updateCallback={onUpdate}
        />
      )}
      <button onClick={() => openModal()} disabled={isModalOpen || loading}>
        Create New Contact
      </button>

      {isModalOpen && (
        <div className="modal" role="dialog" tabIndex={-1}>
          <div className="modal-content">
            <span className="close" onClick={closeModal} role="button" tabIndex={0}>
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
