import React, { Component } from 'react';
import Moment from 'moment';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = { list: [] };
  }

  componentDidMount() {
    fetch(`http://localhost:8000/api/get`)
        .then(result=>result.json())
        .then(items=>this.setState({list: items}))
  }

  render() {
    return (
      <div style={{paddingTop: '100px'}}>
        <table className="table table-striped">
          <thead className="text-center">
            <tr>
              <th>JOB_LOG_PK</th>
              <th>IS_COMPLETE</th>
              <th>SUBMIT_DT</th>
              <th>XPR_JOB_ID</th>
              <th>OVRD_FILE_PATH</th>
              <th>JOB_STATUS</th>
              <th>API_JOB_NAME</th>
              <th>X_RUN_ID</th>
              <th>X_PROCESS_ID</th>
              <th>X_LOG_PATH</th>
              <th>X_SERVER</th>
            </tr>
          </thead>
          <tbody>
            {this.state.list.map(item => (
                <tr>
                  <td className="text-center">{item.JOB_LOG_PK}</td>
                  <td className="text-center">{item.IS_COMPLETE}</td>
                  <td className="text-center">{Moment(item.SUBMIT_DT).format('YYYY/MM/DD HH:mm:ss')}</td>
                  <td className="text-center">{item.XPR_JOB_ID}</td>
                  <td className="text-center">{item.OVRD_FILE_PATH}</td>
                  <td className="text-center">{item.JOB_STATUS}</td>
                  <td className="text-center">{item.API_JOB_NAME}</td>
                  <td className="text-center">{item.X_RUN_ID}</td>
                  <td className="text-center">{item.X_PROCESS_ID}</td>
                  <td className="text-center">{item.X_LOG_PATH}</td>
                  <td className="text-center">{item.X_SERVER}</td>
                </tr>
            ))}
          </tbody>
        </table>

      </div>
    );
  }
}

export default App;
