function HatsList(props) {

    return (
        <table className="table table-striped">
            <thead>
                <tr>
                    <th>Fabric</th>
                    <th>Style Name</th>
                    <th>Color</th>
                    <th>Picture</th>
                    <th>Location</th>
                </tr>
            </thead>
            <tbody>
                {props.hats.map(hats => {
                    return (
                        <tr key={hats.id}>
                            <td>{ hats.fabric }</td>
                            <td>{ hats.style_name }</td>
                            <td>{ hats.color }</td>
                            <td>{ hats.picture_url }</td>
                            <td>{ hats.location }</td>
                        </tr>
                    );
                })}
            </tbody>
        </table>
    )
}

export default HatsList;