import { useState, useEffect } from 'react';
import axios from 'axios';
import Papa from 'papaparse';

function App() {
  const [importData, setImportData] = useState([]);
  const [exportData, setExportData] = useState([]);

  useEffect(() => {
    // Load import.csv
    axios.get('/import.csv')
      .then(response => {
        const parsedData = Papa.parse(response.data, { header: true }).data;
        setImportData(parsedData);
      })
      .catch(error => {
        console.error('Error loading import.csv', error);
      });

    // Load export.csv
    axios.get('/exports.csv')
      .then(response => {
        const parsedData = Papa.parse(response.data, { header: true }).data;
        setExportData(parsedData);
      })
      .catch(error => {
        console.error('Error loading export.csv', error);
      });
  }, []); // This effect runs only once on component mount

  return (
    <div>
      <h1>Top 3 Imported Products</h1>
      <img src="/top_imported_products.png" alt="Top 3 Imported Products" />

      <h1>Imported News</h1>
      <ul>
        {importData.map((item, index) => (
          <li key={index}>
            Review: <a href={item.Link} target="_blank" rel="noopener noreferrer">{item.Review}</a>
          </li>
        ))}
      </ul>

      <h1>Exported News</h1>
      <ul>
        {exportData.map((item, index) => (
          <li key={index}>
            Review: <a href={item.Link} target="_blank" rel="noopener noreferrer">{item.Review}</a>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;