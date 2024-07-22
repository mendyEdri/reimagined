import axios from 'axios';

export interface IHttpClient {
    get<T>(url: string, config?: IAxiosConfig): Promise<T>;
    post<T>(url: string, data: any, config?: IAxiosConfig): Promise<T>;
    delete<T>(url: string, config?: IAxiosConfig): Promise<T>;
}

export interface IAxiosConfig {
    headers?: Record<string, string>;
    params?: Record<string, any>;
}

export class HttpClient implements IHttpClient {
    async get<T>(url: string, config?: IAxiosConfig): Promise<T> {
        const response = await this.request<T>('GET', url, undefined, config);
        return response;
    }

    async post<T>(url: string, data: any, config?: IAxiosConfig): Promise<T> {
        const response = await this.request<T>('POST', url, data, config);
        return response;
    }

    async delete<T>(url: string, config?: IAxiosConfig): Promise<T> {
        const response = await this.request<T>('DELETE', url, undefined, config);
        return response;
    }

    private async request<T>(method: string, url: string, data?: any, config?: IAxiosConfig): Promise<T> {
        const response = await axios({ method, url, data, ...config });
        return response.data;
    }
}