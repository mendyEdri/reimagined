export interface IHttpClient {
    get<T>(url: string, config?: IHttpConfig): Promise<T>;
    post<T>(url: string, data: any, config?: IHttpConfig): Promise<T>;
    delete<T>(url: string, config?: IHttpConfig): Promise<T>;
}

export interface IHttpConfig {
    headers?: Record<string, string>;
    params?: Record<string, any>;
}

export class HttpClient implements IHttpClient {
    async get<T>(url: string, config?: IHttpConfig): Promise<T> {
        const response = await axios.get<T>(url, config);
        return response.data;
    }

    async post<T>(url: string, data: any, config?: IHttpConfig): Promise<T> {
        const response = await axios.post<T>(url, data, config);
        return response.data;
    }

    async delete<T>(url: string, config?: IHttpConfig): Promise<T> {
        const response = await axios.delete<T>(url, config);
        return response.data;
    }
}