import {React,useState} from 'react'
import { Table, TableHead, TableBody, TableRow, TableCell } from '@mui/material';
const PurposiveSampling = () => {
    const [replacement,setReplacement] =useState(false)
    const [data,setData] = useState()
     const [formatt,setFormatt] = useState('')
 const [n,setN] = useState(0)
 const [e,setE] = useState(0)
    const handleSubmit = () =>
    {
           const requestData = new FormData();
  requestData.append('result', 'API');
  requestData.append('data', 'api');
  requestData.append('unit', `40,30,50,30`);
  requestData.append('N', `${n}`);
  requestData.append('e', `${e}`);
  requestData.append('numberOfClusters',`2`);

     const apiUrl = 'http://100102.pythonanywhere.com/api/purposive_sampling/';

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
        <div className='purposive' style={{display:"grid",gap:"1em",marginTop:"1em"}}>
        <div>
        <label>Unit:</label>
        <input/>
        </div>
        <div>
        <label>e:</label>
        <input type='number' onChange={e=>setE(e.target.value)}/>
        </div>
        <div>
        <label/>N:
        <input type='number' onChange={e=>setN(e.target.value)}/>
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

export default PurposiveSampling
