import React from 'react';

class ShoesForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            manufacturer: "",
            modelName: "",
            color: "",
            picturedUrl: "",
            bin: "",
            bins: [],

        }

        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleManufacturerChange = this.handleManufacturerChange.bind(this);
        this.handleModelNameChange = this.handleModelNameChange.bind(this);
        this.handleColorChange = this.handleColorChange.bind(this);
        this.handlePicturedUrlChange = this.handlePicturedUrlChange.bind(this);
        this.handleBinChange = this.handleBinChange.bind(this);
    }


    async handleSubmit(event) {
        event.preventDefault();
        const data = {...this.state};
        data.model_name = data.modelName;
        data.pictured_url = data.picturedUrl;
        delete data.bins;
        delete data.modelName;
        delete data.picturedUrl;
        console.log(data);


        const shoesUrl = 'http://localhost:8080/api/shoes/';
        const fetchConfig = {
            method: "post",
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json',
            },
        };
        const response = await fetch(shoesUrl, fetchConfig);
        if (response.ok) {
            const newShoes = await response.json();
            console.log(newShoes);
            this.setState({
                manufacturer: "",
                modelName: "",
                color: "",
                picturedUrl: "",
                bin: "",
            });
        }
    }


    handleManufacturerChange(event) {
        const value = event.target.value;
        this.setState({ manufacturer: value });
    }

    handleModelNameChange(event) {
        const value = event.target.value;
        this.setState({ model_name: value });
    }

    handleColorChange(event) {
        const value = event.target.value;
        this.setState({ color: value });
    }

    handlePicturedUrlChange(event) {
        const value = event.target.value;
        this.setState({ pictured_url: value });
    }

    handleBinChange(event) {
        const value = event.target.value;
        this.setState({ bin: value});
    }

    async componentDidMount() {
        const url = 'http://localhost:8100/api/bins/';

        const response = await fetch(url);

        if (response.ok) {
            const data = await response.json();
            this.setState({ locations: data.locations });
        }

    }

    render() {
        return (
            <div className="row">
            <div className="offset-3 col-6">
                <div className="shadow p-4 mt-4">
                    <h1>Create new shoes</h1>
                    <form onSubmit={this.handleSubmit} id="create-shoes-form">
                        <div className="form-floating mb-3">
                            <input onChange={this.handleManufacturerChange}
                                value={this.state.manufacturer}
                                placeholder="Manfacturer"
                                required type="text"
                                name="manufacturer"
                                id="manufacturer"
                                className="form-control"/>
                            <label htmlFor="manufacturer">Manufacturer</label>
                        </div>
                        <div className="form-floating mb-3">
                            <input onChange={this.handleModelNameChange}
                                value={this.state.model_name}
                                placeholder="Model"
                                required type="text"
                                name="model"
                                id="model"
                                className="form-control"/>
                            <label htmlFor="name">Model name</label>
                        </div>
                        <div className="form-floating mb-3">
                            <input onChange={this.handleColorChange}
                                value={this.state.color}
                                placeholder="Color"
                                required type="text"
                                name="color"
                                id="color"
                                className="form-control"/>
                            <label htmlFor="color">Color</label>
                        </div>
                        <div className="form-floating mb-3">
                            <input onChange={this.handlePicturedUrlChange}
                                value={this.state.pictured_url}
                                placeholder="Pictured Url"
                                required type="text"
                                name="pictured url"
                                id="pictured url"
                                className="form-control"/>
                            <label htmlFor="pictured_url">Picture Url</label>
                        </div>
                        <div className="mb-3">
                            <select onChange={this.handleBinChange}
                                value={this.state.bin}
                                required name="bin"
                                id="bin"
                                className="form-select">
                                <option value="">Choose a bin</option>
                                {this.state.bin.map(bin => {
                                    return (
                                        <option key={bin.href} value={bin.href}>
                                            {bin.closet_name}
                                        </option>
                                    );
                                })}
                            </select>
                        </div>
                        <button className="btn btn-primary">Create</button>
                    </form>
                </div>
            </div>
        </div>
        );
    }
}

export default ShoesForm;
