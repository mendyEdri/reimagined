import { IHttpClient, IRequestOptions, IResponse } from './IHttpClient';

export class HttpClient implements IHttpClient {
    async get(url: string, options?: IRequestOptions): Promise<IResponse> {
        const response = await fetch(this.buildUrl(url, options?.queryParams), {
            method: 'GET',
            headers: options?.headers,
        });
        const data = await response.json();
        return { status: response.status, data };
    }

    async post(url: string, body: any, options?: IRequestOptions): Promise<IResponse> {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                ...options?.headers,
            },
            body: JSON.stringify(body),
        });
        const data = await response.json();
        return { status: response.status, data };
    }

    async delete(url: string, options?: IRequestOptions): Promise<IResponse> {
        const response = await fetch(url, {
            method: 'DELETE',
            headers: options?.headers,
        });
        const data = await response.json();
        return { status: response.status, data };
    }

    private buildUrl(url: string, queryParams?: Record<string, string>): string {
        if (!queryParams) return url;
        const query = new URLSearchParams(queryParams).toString();
        return `${url}?${query}`;
    }
}