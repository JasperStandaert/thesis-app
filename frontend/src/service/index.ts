import axios from 'axios'

export default class HttpService{

    basepath = '127.0.0.1:5000'

    getPatient(patientId: string) {
        return axios.get(this.basepath + '/getpatient/' + patientId);
    }
}