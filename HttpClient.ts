export interface IHttpClient {
    get<T>(url: string): Promise<T>;
    post<T, U>(url: string, data: T): Promise<U>;
    delete<T>(url: string): Promise<T>;
}

export class HttpClient implements IHttpClient {
    async get<T>(url: string): Promise<T> {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json() as Promise<T>;
    }

    async post<T, U>(url: string, data: T): Promise<U> {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json() as Promise<U>;
    }

    async delete<T>(url: string): Promise<T> {
        const response = await fetch(url, {
            method: 'DELETE',
        });
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json() as Promise<T>;
    }
}