import React from 'react';
 

const NavBar = () => {
    const apiurl=import.meta.env.VITE_BACKEND_API;
  
    if (!apiurl) {
        console.error("API URL is not defined! Please check your .env file.");
    }

    return (
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
            <div className="container-fluid">
                <a className="navbar-brand" href="/">
                    <img 
                        src="https://getbootstrap.com/docs/4.0/assets/brand/bootstrap-solid.svg" 
                        width="30" 
                        height="30" 
                        className="d-inline-block align-top" 
                        alt="" 
                    />
                    HealthCare
                </a>
                <button 
                    className="navbar-toggler" 
                    type="button" 
                    data-toggle="collapse" 
                    data-target="#navbarNav" 
                    aria-controls="navbarNav" 
                    aria-expanded="false" 
                    aria-label="Toggle navigation"
                >
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarNav">
                    <div className="navbar-nav">
                        <a className="nav-link active" aria-current="page" href="/">Home</a>
                        <a className="nav-link" href="/patient-records">Patient Records</a>            
                    </div>                    
                </div>
            </div>
        </nav>
    );
};

export default NavBar;
