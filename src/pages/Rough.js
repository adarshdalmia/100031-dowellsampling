import React, { useEffect } from 'react';

function Rough() {
  const requestData = new FormData();
  requestData.append('populationSize', '3');
  requestData.append('data', 'api');
  requestData.append('replacement', 'true');
  requestData.append('samplingType', 'geometricalApproach');
  requestData.append('allocationType', 'equal');

  useEffect(() => {
    const apiUrl = 'http://100102.pythonanywhere.com/api/stratified/';

    fetch(apiUrl, {
      method: 'POST',
      body: requestData,
    })
      .then(response => response.json())
      .then(data => {
        console.log(data); // Logging the response data
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }, []);

  return (
    <div className="App">
      {/* Your component content */}
    </div>
  );
}

export default Rough;
