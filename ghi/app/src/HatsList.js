// function HatsList(props) {

//     return (
//         <table className="table table-striped">
//             <thead>
//                 <tr>
//                     <th>Fabric</th>
//                     <th>Style Name</th>
//                     <th>Color</th>
//                     <th>Picture</th>
//                     <th>Location</th>
//                 </tr>
//             </thead>
//             <tbody>
//                 {props.hats.map(hats => {
//                     return (
//                         <tr key={hats.id}>
//                             <td>{ hats.fabric }</td>
//                             <td>{ hats.style_name }</td>
//                             <td>{ hats.color }</td>
//                             <td>{ hats.picture_url }</td>
//                             <td>{ hats.location }</td>
//                         </tr>
//                     );
//                 })}
//             </tbody>
//         </table>
//     )
// }

// export default HatsList;

import React, { useState, setItems } from "react";
import { Link } from 'react-router-dom';

function HatsList(props) {
    const [items, setItems] = React.useState(props.hats);
    const deleteItem = (id) => async () => {
        const url = `http://localhost:8090/api/hats/${id}`;
        const fetchConfig = {
            method: "delete"
        }
        const response = await fetch(url, fetchConfig)
        if (response.ok) {
            const deleted = await response.json();
        }
        setItems((items) => items.filter(item => {
            return item.id !== id}));
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
          {items.map(hat => {
            return (
              <tr key={hat.id}>
                <td>{ hat.fabric }</td>
                <td>{ hat.style_name }</td>
                <td>{ hat.color }</td>
                <td>{ hat.picture_url }</td>
                <td>{ hat.location }</td>
                <td><button onClick={deleteItem(hat.id)}>Delete</button></td>
              </tr>
            );
          })}
        </tbody>
      </table>
      <div className="d-grid gap-2 d-sm-flex justify-content-sm-center">
        <Link to="/hats/new" className="btn btn-primary btn-lg px-4 gap-3">Create a new hat</Link>
      </div>
      </>
    );
  }
  



  export default HatsList;