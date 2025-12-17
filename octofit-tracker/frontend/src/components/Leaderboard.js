
import React, { useEffect, useState } from 'react';

const Leaderboard = () => {
  const [entries, setEntries] = useState([]);
  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;

  useEffect(() => {
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setEntries(results);
        console.log('Leaderboard endpoint:', apiUrl);
        console.log('Fetched leaderboard:', results);
      });
  }, [apiUrl]);

  return (
    <div className="card shadow-sm">
      <div className="card-body">
        <h2 className="card-title mb-4 text-success">Leaderboard</h2>
        <div className="table-responsive">
          <table className="table table-striped table-hover align-middle">
            <thead className="table-dark">
              <tr>
                <th scope="col">#</th>
                <th scope="col">User ID</th>
                <th scope="col">Score</th>
              </tr>
            </thead>
            <tbody>
              {entries.length === 0 ? (
                <tr><td colSpan="3" className="text-center">No leaderboard entries found.</td></tr>
              ) : (
                entries.map((entry, idx) => (
                  <tr key={idx}>
                    <th scope="row">{idx + 1}</th>
                    <td>{entry.user_id}</td>
                    <td>{entry.score}</td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Leaderboard;
