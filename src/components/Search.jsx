
import React, { useState } from 'react'


const Search = () => {
  const [data,setData] = useState('');
  const [popSize,setPopSize]=useState(0);
  const[error,setError]=useState(0);
  const [confidenceLevel,setConfidenceLevel]=useState(0.90);
  const[sDeviation,setSDeviation]=useState(null)
  const [toggle,setToggle] = useState(false)
  
const handleSubmit =async () => 
{

    if(popSize <= 0 || error <=0)
    {
      alert("Invalid input. Population size and error must be positive")
    }
    else{
    const data =
    {
    population_size:popSize,
    error, 
    confidence_level:confidenceLevel,
    standard_deviation:sDeviation
    }
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
    }
      // console.log(data);
    
  })
  .catch((error) => {
    // Handle any errors that occurred during the request
  });
 
    }

}

    return (
    <>
  
<div  style={{display:"grid",justifyContent:"center",marginTop:"10pc"}}>
   <label>Population Size</label>
    <input type='number' min="10" value={popSize} placeholder='Population Size' onChange={(e)=>setPopSize(e.target.value)} style={{width:"200px"}}/>
    <label>Error</label>
    <input type='number' placeholder='Error' value={error} onChange={(e)=>setError(e.target.value)} style={{width:"200px"}}/>
    <label>Confidence Level</label>
 <select onChange={(e)=>setConfidenceLevel(e.target.value)}>
  <option disabled>--select--</option>
  <option>0.90</option>
  <option>0.95</option>
  <option>0.99</option>
 </select>
    <label>Standard Deviation</label>
    <input type='number' placeholder='Standard Deviation' onChange={(e)=>setSDeviation(e.target.value)} style={{width:"200px"}}/>
 
<button className='btn btn-primary' style={{width:"200px"}} onClick={handleSubmit}>Search</button>
{toggle  && 
<>
<h2 style={{marginTop:"2em",display:"grid",justifyContent:"center"}}>Response</h2>
<h4>Method Used : {data.method_used}</h4>
<h4>Process Time : {data.process_time}</h4>
<h4>Sample Size : {data.sample_size}</h4>
</>}
</div>
  </>
  )
}

export default Search
