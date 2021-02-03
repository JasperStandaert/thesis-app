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
    public getInteractions(name: string){
        return axios.get(this.basepath + '/get_patient_interactions/' + name)
    }
    public createGraph(name: string){
        return axios.get(this.basepath + '/create_patient_graph/' + name, {
            headers: {
                'Content-Type': 'application/json',
            },
        });
    }

    public addDrug(patient: any, drug: any){
        return axios.post(this.basepath + "/add_drug_for_patient/"+ patient + "/" + drug);
    }
    public postPatient(patient: any){
        return axios.post(this.basepath + "/add_patient", patient, {
            headers: {
                'Content-Type': 'application/json'
            },
        });
    }
    public removeDrug(patient: string, drug: any){
        return axios.delete(this.basepath + "/remove_drug_for_patient/" + patient + "/" + drug);
    }
    public removePatient(patient: string){
        return axios.delete(this.basepath + "/remove_patient/" + patient);
    }   
}
