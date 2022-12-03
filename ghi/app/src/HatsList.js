function HatsList(props) {

    return (
        <table className="table table-striped">
            <thead>
                <tr>
                    <th>Fabric</th>
                    <th>Style Name</th>
                    <th>Color</th>
                    <th>Picture</th>
                </tr>
            </thead>
            <tbody>
                {items.map((hats) => {
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