import React, { useState, useEffect } from "react";
import { Link } from 'react-router-dom';
import './index.css';




function HatsList() {
    const [hats, setHats] = useState([]);
    const getHats = async () => {
        const hatsUrl = "http://localhost:8090/api/hats/";
        const response = await fetch(hatsUrl);

        if (response.ok) {
            const listHats = await response.json();
            setHats(listHats.hats);
      }
    };
    useEffect(() => {getHats()}, []);
    const deleteHat = (id) => async () => {


      try {
        const url = `http://localhost:8090/api/hats/${id}/`;
        const deleteResponse = await fetch(url, 
            { 
                method: "delete" 
            }
        );
        if (deleteResponse.ok) {
          const refreshUrl = "http://localhost:8090/api/hats/";
          const reloadResponse = await fetch(refreshUrl);
          const newHats = await reloadResponse.json();
          setHats(newHats.hats);
        }
      } 
      catch (err) {
      }
    };
    if (hats === undefined) {
      return null;
    }


    return (
      <>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Fabric</th>
            <th>Style Name</th>
            <th>Color</th>
            <th>Picture</th>
            <th>Location</th>
            <th>Delete</th>
          </tr>
        </thead>
        <tbody>
          {hats.map((hats) => {
            return (
              <tr key={hats.id}>
                <td>{ hats.fabric }</td>
                <td>{ hats.style_name }</td>
                <td>{ hats.color }</td>
                <td><img src={ hats.picture_url } /></td>
                <td>{ hats.location }</td>
                <td><button className="circle" onClick={deleteHat(hats.id)}>Delete</button></td>
              </tr>
            );
          })}
        </tbody>
      </table>
      <div className="d-grid gap-2 d-sm-flex justify-content-sm-center">
      </div>
      </>
    );
  }
  



  export default HatsList;