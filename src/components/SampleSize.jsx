import React, { useState } from 'react'
import ClipLoader from "react-spinners/ClipLoader";
import { Table, TableHead, TableBody, TableRow, TableCell } from '@mui/material';
const SampleSize = () => {
  
  const [checkPop,setCheckPop] = useState('No2')
  const [known,setKnown] = useState('No2')
  const [sKnown,setSKnown] = useState('N3o')
  const [calc,setCalc] = useState(false)
  const[error,setError]=useState(0.5);
  const [popSize,setPopSize] =useState(0)
  const[sDeviation,setSDeviation]=useState(null)
  const [data,setData] = useState('');
  const [toggle,setToggle] = useState(false)
  const [confidenceLevel,setConfidenceLevel]=useState(0.90);
  const [buttonClicked,setButtonClicked] = useState(false)
    
const handleSubmit =async () => 
{
    
    if(popSize <= 0)
    {
      alert("Invalid input. Population size and error must be positive")
    }
    else{
setButtonClicked(true)
var data =
    {
    population_size:popSize,
    error,
    standard_deviation:sDeviation,confidence_level : confidenceLevel 
    }
console.log(data)
 fetch("https://100102.pythonanywhere.com/sample-size/", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify(data),
})

  .then((response) => response.json())
  .then((data) => {
    if(data.error)
    {
      alert("Invalid input. Population size and error must be positive")
    }
    else
    {

      setData(data)
      setToggle(true)
      setButtonClicked(false)
    }
      console.log(data);
    
  })
  .catch((error) => {
    // Handle any errors that occurred during the request
  });
 
    }

}

  return (
    
    <div style={{display:"grid",justifyContent:"center",marginTop:"10pc",gap:"0.5em"}}>
      <h3>Sample Size Function</h3>
      <label className="form-label">Do you have Population Size?</label>
      <select className="form-control form-control-lg" onChange={e=>setCheckPop(e.target.value)}>
        <option>Select One</option>
        <option>Yes</option>
        <option>No</option>
      </select>
  {
    checkPop==="Yes" ?
    <>
      <label className="form-label">Is Population Size known?</label>
      <select className="form-control form-control-lg" onChange={e=>setKnown(e.target.value)}>
          <option>Select One</option>
        <option>Yes</option>
        <option>No</option>
      </select>
      {known === 'Yes' &&
      <>
      <label className="form-label">Population Size</label>
      <input  class="form-control" placeholder='Enter N' type='number' onChange={e=>setPopSize(e.target.value)}/>
        <label className="form-label">Error</label>
       <input type='number' className="form-control form-control-lg" placeholder='Error' value={error} onChange={(e)=>setError(e.target.value)} style={{width:"200px"}}/>
        <label className="form-label">Confidence Level</label> 
       <select className="form-control form-control-lg" onChange={(e)=>setConfidenceLevel(e.target.value)}>
  <option disabled>--select--</option>
  <option>0.90</option>
  <option>0.95</option>
  <option>0.99</option>
 </select>
       <label className="form-label">Is standard deviation known?</label>
      <select className="form-control form-control-lg" onChange={e=>setSKnown(e.target.value)}>
        <option>Select One</option>
        <option>Yes</option>
        <option>No</option>
      </select>
    {
        sKnown === 'Yes' ?
        <>
        <input class="form-control" placeholder='Enter Standard Deviation' onChange={e=>setSDeviation(e.target.value)} type='number'/>
        </>
        :
        <>
        </>
    }
      </>
    }
     
    </>

    :
    
    <>
 { checkPop === "No" ?
    <>
    <label className="form-label">Is standard deviation known?</label>
      <select className="form-control form-control-lg" onChange={e=>setSKnown(e.target.value)}>
        <option>Select One</option>
        <option>Yes</option>
        <option>No</option>
      </select>
    {
        sKnown === 'Yes' ?
        <>
          <label className="form-label">Standard Deviation</label>
        <input  class="form-control" placeholder='Enter Standard Deviation' onChange={e=>setSDeviation(e.target.value)} type='number'/>
        </>
        :
        <>
        </>
    }
    </>
    :<>
    
    </>
}
    </>
}
 <button onClick={handleSubmit} className="btn btn-primary">Submit</button>
 {!toggle && buttonClicked &&
 
     <div style={{marginLeft:"30%",justifyContent:"center"}}> 
      <ClipLoader
        color="green"
        loading={true}
        size={50}
        aria-label="Loading Spinner"
        data-testid="loader"
      />
      </div>
 
 }
 {toggle  && 
 
<>
<h2 style={{marginTop:"2em",display:"grid",justifyContent:"center"}}>Response</h2>
  <Table className="styled-table">
          <TableHead>
            <TableRow >
              <TableCell style={{fontWeight:"bolder"}}>Sample Size</TableCell>
              <TableCell style={{fontWeight:"bolder"}}>Process Time</TableCell>
              <TableCell style={{fontWeight:"bolder"}}>Method Used</TableCell>
              {/* Add more TableCell elements for additional columns */}
            </TableRow>
          </TableHead>
          <TableBody>
            <TableRow>
              <TableCell>{data.sample_size}</TableCell>
              <TableCell>{data.process_time}</TableCell>
              <TableCell>{data.method_used}</TableCell>
              {/* Add more TableCell elements for additional columns */}
            </TableRow>
          </TableBody>
          </Table>
</>



}
    </div>
  )
}

export default SampleSize
