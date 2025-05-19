import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [backendMessage, setBackendMessage] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:5000/api/message')
      .then(response => {
        setBackendMessage(response.data.message);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching message:', error);
        setError('Failed to fetch message');
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>{error}</p>;

  return (
    <div>
      <p>Frontend Connected to Backend</p>
      <p>Backend says: {backendMessage}</p>
    </div>
  );
}

export default App;
