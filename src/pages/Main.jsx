import { Checkbox } from '@mui/material'
import React from 'react'
import { useState } from 'react'
import StratifiedSampling from '../components/StratifiedSampling';
import ClusterSampling from '../components/ClusterSampling';
import PurposiveSampling from '../components/PurposiveSampling';
import SimpleRandomSampling from '../components/SimpleRandomSampling';

const Main = () => {
    const[sampling,setSampling] = useState('');
   
 
  return (
    <div style={{display:"grid",justifyContent:"center"}}>
    <div style={{width:"80em"}}>
      <h1>Sampling Inputs</h1>
      <p>Sampling Type:</p>
    <select onChange={e=>setSampling(e.target.value)}  className="form-control form-control-lg"
      style={{ width: '100%', height: '50px', fontSize: '18px' }}>
        <option>Select Sampling Type</option>
        <option>Stratified Sampling</option>
        <option>Systematic Sampling</option>
        <option>Simple Random Sampling</option>
        <option>Cluster Sampling</option>
        <option>Purposive Sampling</option>
    </select>
    {sampling === "Stratified Sampling" ?
   <StratifiedSampling/>
    :
   sampling === "Systematic Sampling" ?
    <div className='systematic' style={{marginTop:"1em"}}>
        <label>Population Size:</label>
        <input/>
    </div>
    :
   sampling === "Simple Random Sampling" ?
    <SimpleRandomSampling/>
:
sampling === "Cluster Sampling" ?
    <ClusterSampling/>
:
sampling === "Purposive Sampling" &&
  <PurposiveSampling/>

  }

  </div>
  </div>
  )
}

export default Main
