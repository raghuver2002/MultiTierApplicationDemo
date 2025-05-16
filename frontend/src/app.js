import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [backendMessage, setBackendMessage] = useState('');

  useEffect(() => {
    axios.get('/api/message')
      .then((response) => {
        setData(response.data);
        setLoading(false);
        console.log('API Response:', response.data);
        setBackendMessage(response.data.message);
      })
      .catch(error => {
        setData(err.message);
        setLoading(false);
        console.error('Error fetching message:', error);
      });
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <p>Frontend Connected to Backend</p>
      <p>Backend says: {backendMessage}</p>
    </div>
  );
}

export default App;