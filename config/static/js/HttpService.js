// ! SINGLETON
class HTTPService {
    constructor() {
        if (HTTPService.instance) {
            return HTTPService.instance;
        }
        HTTPService.instance = this;
        this.BASE_URL = 'http://127.0.0.1:5000/api';
    }

    async get(endpoint, callback) {
        try {
            const url = `${this.BASE_URL}${endpoint}`;
            const response = await axios.get(url);
            console.log("HTTPService GET");
            console.log("Url: " + url);
            console.log("response: ", response);
            callback(null, response.data);
        } catch (error) {
            callback(error, null);
        }
    }

    async post(endpoint, data, callback) {
        try {
            const response = await axios.post(`${this.BASE_URL}${endpoint}`, data);
            console.log("HTTPService POST");
            console.log("response: ", response);
            callback(null, response.data);
        } catch (error) {
            callback(error, null);
        }
    }
}

export default HTTPService;