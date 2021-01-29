import axios from 'axios';

export default class HttpService {

    public basepath = 'http://127.0.0.1:5000';

    public getPatients() {
        return axios.get(this.basepath + '/get_all_patients', {
            headers: {
                'Content-Type': 'application/json',
            },
        });
    }
    public getMedication() {
        return axios.get(this.basepath + '/get_all_drugs', {
            headers: {
                'Content-Type': 'application/json',
            },
        });
    }
}
