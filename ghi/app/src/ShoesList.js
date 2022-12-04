import React from 'react';

function ShoesList(props) {
    const [items, setItems] = React.useState(props.shoes);
    const deleteItem = (id) => async () => {
        const url = `http://localhost:8080/api/shoes/${id}`;
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
        console.log(items)


    return (
        <table className="table table-striped">
            <thead>
                <tr>
                    <th>Manufacturer</th>
                    <th>Model</th>
                    <th>Color</th>
                    <th>Picture Url</th>
                    <th>Bin</th>
                </tr>
            </thead>
            <tbody>
                {items.props.shoes.map(shoes => {
                    return (
                        <tr key={ shoes.id }>
                            <td>{ shoes.manufacturer }</td>
                            <td>{ shoes.model_name }</td>
                            <td>{ shoes.color }</td>
                            <td>{ shoes.pictured_url }</td>
                            <td>{ shoes.bin }</td>
                            <td><button onClick={deleteItem(shoes.id)}>Delete</button></td>
                        </tr>
                    );
                })}
            </tbody>
        </table>
    );
}

export default ShoesList;
