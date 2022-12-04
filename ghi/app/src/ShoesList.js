function ShoesList(props) {
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
                {props.shoes.map(shoes => {
                    return (
                        <tr key={ shoes.id }>
                            <td>{ shoes.manufacturer }</td>
                            <td>{ shoes.model_name }</td>
                            <td>{ shoes.color }</td>
                            <td>{ shoes.pictured_url }</td>
                            <td>{ shoes.bin }</td>
                        </tr>
                    );
                })}
            </tbody>
        </table>
    );
}

export default ShoesList;
