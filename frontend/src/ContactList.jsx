import React, { useState } from "react";

const ContactList = ({ contacts, updateContact, updateCallback }) => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const onDelete = async (id) => {
    const confirmDelete = window.confirm("Are you sure you want to delete this contact?");
    if (!confirmDelete) return;

    setLoading(true);
    try {
      const response = await fetch(`http://127.0.0.1:5000/delete_contact/${id}`, {
        method: "DELETE",
      });

      if (response.status === 200) {
        updateCallback();
      } else {
        setError("Failed to delete the contact. Please try again.");
      }
    } catch (err) {
      setError("An error occurred while deleting the contact.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      {error && <div className="error">{error}</div>}
      <table>
        <thead>
          <tr>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Email</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {contacts.map((contact) => (
            <tr key={contact.id}>
              <td>{contact.firstName}</td>
              <td>{contact.lastName}</td>
              <td>{contact.email}</td>
              <td>
                <button onClick={() => updateContact(contact)}>Update</button>
                <button onClick={() => onDelete(contact.id)} disabled={loading}>
                  {loading ? "Deleting..." : "Delete"}
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ContactList;
