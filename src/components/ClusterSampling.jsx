import React, { useRef, useState } from 'react'
import { Table, TableHead, TableBody, TableRow, TableCell } from '@mui/material';
const ClusterSampling = () => {
   const insertedID = useRef()
    const [replacement,setReplacement] =useState(false)
    const popSize = useRef()
    const [e,setE] = useState(0)
    const [data,setData] = useState()
     const [formatt,setFormatt] = useState('')
 
    const handleSubmit = () =>
    {
  console.log(replacement)

  console.log(popSize.current.value)
           const requestData = new FormData();
  requestData.append('populationSize', '3');
  requestData.append('data', 'api');
  requestData.append('replacement', 'true');
  requestData.append('samplingType', 'geometricalApproach');
  requestData.append('allocationType', 'equal');
  requestData.append('numberOfClusters', '2');
  requestData.append('e', `${e}`);
  requestData.append('result', 'API');
  requestData.append('sizeOfCluster', '40');

     const apiUrl = 'http://100102.pythonanywhere.com/api/cluster_sampling/';

    fetch(apiUrl, {
      method: 'POST',
      body: requestData,
    })
      .then(response => response.json())
      .then(data => {
        console.log(data);
        setData(data) // Logging the response data
      })
      .catch(error => {
        console.error('Error:', error);
      });
    
    }
  
  return (
    <div>
      <div className='cluster' style={{display:"grid",gap:"1em",marginTop:"1em"}}>
        <div>
        <label>population_size:</label>
        <input ref={popSize}/>
        </div>
        <div>
        <label>e:</label>
        <input onChange={e=>setE(e.target.value)}/>
        </div>
        <div>
        <label>M:</label>
        <input/>
        </div>
        <div>
        <label>hi:</label>
        <input/>
        </div>
    </div>
    <div style={{marginTop:"1em"}}>
    <label>Select Upload Format:</label>
    <select onChange={e=>setFormatt(e.target.value)}>
        <option>Select Format</option>
        <option>API</option>
        <option>File</option>
    </select>
    {formatt === "File" && 
    <div style={{marginTop:"1em"}}>
        <label>Add Excel File:</label>
        <input type='file' accept='.xlsx'/>
    </div>
    }
</div>
<button className='btn btn-primary' onClick={handleSubmit} style={{marginTop:"1em"}}>Submit</button>
{data && 
    <Table className="styled-table">
          <TableHead>
            <TableRow>
              <TableCell>Column 1</TableCell>
              <TableCell>Column 2</TableCell>
              <TableCell>Column 3</TableCell>
              {/* Add more TableCell elements for additional columns */}
            </TableRow>
          </TableHead>
          <TableBody>
            {data && data.samples?.map((innerArray, outerIndex) => (
              <TableRow key={outerIndex}>
                {innerArray.map((item, innerIndex) => (
                  <TableCell key={innerIndex}>
                    {/* Render your item content here */}
                    {item.map((i)=>
                    <>
                    {i},
                    </>)}
                  </TableCell>
                ))}
              </TableRow>
            ))}
          </TableBody>
        </Table>
}

    </div>
  )
}

export default ClusterSampling
