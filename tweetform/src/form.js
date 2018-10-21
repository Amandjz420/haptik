import React, { Component } from 'react';
import axios from 'axios'

export class NameForm extends Component {
    constructor(props) {
        super(props);
        this.state = {
            title: "",
            msg: "",
            people_id: 1,

        };


        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChangeTitle = this.handleChangeTitle.bind(this);
        this.handleChangeMsg = this.handleChangeMsg.bind(this);
    }
    handleChangeTitle(event) {
        this.setState({title: event.target.value})
    }
    handleChangeMsg(event) {
        this.setState({msg: event.target.value})
    }
    handleSubmit(e) {
        e.preventDefault();
        const data = {
            title: this.state.title,
            msg: this.state.msg,
            people_id: this.state.people_id
        };
        let headers = {
            'Content-Type': 'application/json',
            'Authorization': 'token 75e5639339a65e97dfe93a9a9e6b0d7e86c4c090'
        };
        axios.post(`https://127.0.0.1:8000/api/tweets/`, { data }, {headers: headers})
            .then(res => {
                alert(res.data);

            });
        this.setState({title: "", msg: ""})
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <row>
                    <label className="title">
                        Title:
                        <input type="text" name="title" value={this.state.title} onChange={this.handleChangeTitle} />
                    </label>
                </row>
                <br />
                <row>
                    <label className="content">
                        Message:
                        <input type="text" name="Message" value={this.state.msg} onChange={this.handleChangeMsg}/>
                    </label>
                </row>
                <br />
                <input type="submit" value="Submit" />
            </form>
        );
    }
}