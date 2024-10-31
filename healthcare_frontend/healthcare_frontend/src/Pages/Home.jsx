import React, { useState } from "react";

const Home = () => {
  const apiurl = import.meta.env.VITE_BACKEND_API;
  const [error, setError] = useState('');
  const [file, setFile] = useState(null);
  const [modalVisible, setModalVisible] = useState(false);
  const [modalMessage, setModalMessage] = useState('');

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];

    if (selectedFile) {
      // Validar extensión de archivo
      if (!selectedFile.name.endsWith('.xls') && !selectedFile.name.endsWith('.xlsx')) {
        setError('Please select an Excel file.');
        setFile(null);
      } else {
        setError('');
        setFile(selectedFile); // Establece el archivo si es válido
        console.log(selectedFile.name);
      }
    }
  };

  const handleUpload = async (event) => {
    event.preventDefault(); // Evita la recarga de la página
    
    if (!file) {
      setError('No file selected.');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);
    
    try {
      const response = await fetch(`${apiurl}process-file/`, {
        method: 'POST',
        headers: {
          'accept': 'application/json'
        },
        body: formData
      });

      if (response.ok) {
        const data = await response.json();
        console.log('Response:', data.data);
        // Mostrar mensaje en el modal
        setModalMessage('File uploaded: '+data.data);
        setModalVisible(true);
      } else {
        console.error('Upload failed:', response.statusText);
        setModalMessage('Upload failed. Please try again.');
        setModalVisible(true);
      }
    } catch (error) {
      console.error('Error uploading file:', error);
      setModalMessage('An error occurred while uploading the file.');
      setModalVisible(true);
    }
  };

  const handleCloseModal = () => {
    setModalVisible(false);
  };

  return (
    <div className="container">
      <div className="row" style={{ height: "100vh" }}>
        <div className="col d-flex justify-content-center align-items-center flex-column">
          <h1>Welcome to HealthCare System</h1>
          <div className="mb-3">
            <label htmlFor="formFile" className="form-label">Choose a Patient Data File to Upload</label>
            <input 
              className="form-control" 
              type="file" 
              id="formFile" 
              accept=".xls, .xlsx" 
              onChange={handleFileChange} // Conectar el evento onChange
            />
          </div>
          {error && <p className="text-danger">{error}</p>}
          <button className="btn btn-primary" onClick={handleUpload}>Upload File</button>
        </div>
      </div>

      {/* Modal */}
      {modalVisible && (
        <div className="modal fade show" style={{ display: 'block' }} tabIndex="-1" role="dialog">
          <div className="modal-dialog" role="document">
            <div className="modal-content">
              <div className="modal-header">
                <h5 className="modal-title">Upload Status</h5>
                <button type="button" className="close" onClick={handleCloseModal}>
                  <span>&times;</span>
                </button>
              </div>
              <div className="modal-body">
                <p>{modalMessage}</p>
              </div>
              <div className="modal-footer">
                <button type="button" className="btn btn-secondary" onClick={handleCloseModal}>Close</button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Home;
