import React, { useEffect, useState } from 'react';
import axios from 'axios';

const PatientRecordsTable = ({ records }) => (
  <table className="table table-striped table-bordered table-hover">
    <thead className="thead-dark">
      <tr>
        <th>Patient</th>
        <th>Labcode</th>
        <th>Project</th>
        <th>Cohort</th>
        <th>CaseId</th>
        <th>Center</th>
        <th>CenterCode</th>
        <th>TrialCode</th>
        <th>External Id</th>
        <th>Specie</th>
        <th>Consent</th>
        <th>Disease</th>
        <th>Evolutive Stage</th>
        <th>Diagnosis State</th>
        <th>Diagnosis Date</th>
        <th>Inclusion Date</th>
      </tr>
    </thead>
    <tbody>
      {records.map((record) => (
        <tr key={record.Patient + '|' + record.Labcode}>
          <td>{record.Patient}</td>
          <td>{record.Labcode}</td>
          <td>{record.Project}</td>
          <td>{record.Cohort}</td>
          <td>{record.CaseId}</td>
          <td>{record.Center}</td>
          <td>{record.CenterCode}</td>
          <td>{record.TrialCode}</td>
          <td>{record.ExternalId}</td>
          <td>{record.Specie}</td>
          <td>{record.Consent}</td>
          <td>{record.Disease}</td>
          <td>{record.EvolutiveStage}</td>
          <td>{record.DiagnosisState}</td>
          <td>{record.DiagnosisDate}</td>
          <td>{record.InclusionDate}</td>
        </tr>
      ))}
    </tbody>
  </table>
);

const PatientRecords = () => {
  const [records, setRecords] = useState([]);
  const [searchWord, setSearchWord] = useState('');
  const [currentPage, setCurrentPage] = useState(1);
  const [perPage, setPerPage] = useState(10);
  const [sortBy, setSortBy] = useState('InclusionDate');
  const [sortOrder, setSortOrder] = useState('asc');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const apiurl = import.meta.env.VITE_BACKEND_API;

  const fetchData = async () => {
    setIsLoading(true);
    setError(null);
    try {
      const response = await axios.get(`${apiurl}patient-record/`, {
        params: {
          page: currentPage,
          per_page: perPage,
          sort_by: sortBy,
          sort_order: sortOrder,
          search: searchWord,
        },
      });
      setRecords(response.data);
    } catch (err) {
      console.error('Error fetching data:', err);
      setError('Failed to fetch records');
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, [searchWord, currentPage, perPage, sortBy, sortOrder]);

  return (
    <div className="container-fluid">
      <h2 className="mb-4">Patient Records</h2>

      <div className="form-group">
        <label htmlFor="search_word">Search</label>
        <input
          className="form-control"
          id="search_word"
          type="text"
          placeholder="Search"
          value={searchWord}
          onChange={(e) => setSearchWord(e.target.value)}
        />
      </div>

      <div className="form-group">
        <label htmlFor="per_page">Items per page</label>
        <select
          id="per_page"
          className="form-control"
          value={perPage}
          onChange={(e) => setPerPage(Number(e.target.value))}
        >
          <option value={10}>10</option>
          <option value={20}>20</option>
          <option value={50}>50</option>
        </select>
      </div>

      <div className="form-group">
        <label htmlFor="sort_by">Sort by</label>
        <select
          id="sort_by"
          className="form-control"
          value={sortBy}
          onChange={(e) => setSortBy(e.target.value)}
        >
          <option value="Patient">ID</option>
          <option value="DiagnosisDate">Inclusion Date</option>
          <option value="InclusionDate">Diagnosis Date</option>
        </select>
      </div>

      <div className="form-group">
        <label htmlFor="sort_order">Sort order</label>
        <select
          id="sort_order"
          className="form-control"
          value={sortOrder}
          onChange={(e) => setSortOrder(e.target.value)}
        >
          <option value="asc">Ascending</option>
          <option value="desc">Descending</option>
        </select>
      </div>

      {isLoading ? (
        <p>Loading records...</p>
      ) : error ? (
        <p className="text-danger">{error}</p>
      ) : (
        <PatientRecordsTable records={records} />
      )}

      <div className="pagination">
        <button
          className="btn btn-secondary"
          onClick={() => setCurrentPage((prev) => Math.max(prev - 1, 1))}
          disabled={currentPage === 1}
        >
          Previous
        </button>
        <span className="mx-2">Page {currentPage}</span>
        <button
          className="btn btn-secondary"
          onClick={() => setCurrentPage((prev) => prev + 1)}
        >
          Next
        </button>
      </div>
    </div>
  );
};

export default PatientRecords;
