import { useState } from 'react'
import './App.css'
import NavBar from './Navbar'
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Home from './Pages/Home';

import PatientRecords from './Pages/PatientRecords';

function App() {
  return (

     <Router>
       <NavBar />
       <Routes>
         <Route path="/" element={<Home />} />
         <Route path="/patient-records" element={<PatientRecords />} />
       </Routes>
     </Router>
      
   
  )
}
//<Route path='/Records' element={<Records/>} />
export default App