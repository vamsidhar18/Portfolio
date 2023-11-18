
import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [profileData, setProfileData] = useState(null);

  useEffect(() => {
    fetch('/api/profile')
      .then(response => response.json())
      .then(data => setProfileData(data))
      .catch(error => console.error('Error fetching data: ', error));
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        {profileData ? (
          <div>
            <h1>{profileData.name}</h1>
            <p>Location: {profileData.location}</p>
            <h2>Education</h2>
            {profileData.education.map((edu, index) => (
              <div key={index}>
                <h3>{edu.degree}</h3>
                <p>{edu.institution} ({edu.period})</p>
                <strong>Coursework:</strong>
                <ul>
                  {edu.coursework.map((course, idx) => <li key={idx}>{course}</li>)}
                </ul>
              </div>
            ))}
            {/* Additional sections for technical skills, projects, etc. */}
          </div>
        ) : (
          <p>Loading profile...</p>
        )}
      </header>
    </div>
  );
}

export default App;
