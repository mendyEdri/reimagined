import { HttpClient } from './HttpClient';

describe('HttpClient', () => {
    let httpClient: HttpClient;

    beforeEach(() => {
        httpClient = new HttpClient();
    });

    afterEach(() => {
        jest.clearAllMocks();
    });

    describe('get', () => {
        it('should call fetch with the correct URL', async () => {
            const url = 'https://api.example.com/data';
            global.fetch = jest.fn().mockResolvedValue({
                ok: true,
                json: jest.fn().mockResolvedValue({}),
            });

            await httpClient.get(url);

            expect(fetch).toHaveBeenCalledWith(url);
        });

        it('should throw an error if the response is not ok', async () => {
            const url = 'https://api.example.com/data';
            global.fetch = jest.fn().mockResolvedValue({
                ok: false,
            });

            await expect(httpClient.get(url)).rejects.toThrow('Network response was not ok');
        });
    });

    describe('post', () => {
        it('should call fetch with the correct URL and data', async () => {
            const url = 'https://api.example.com/data';
            const data = { key: 'value' };
            global.fetch = jest.fn().mockResolvedValue({
                ok: true,
                json: jest.fn().mockResolvedValue({}),
            });

            await httpClient.post(url, data);

            expect(fetch).toHaveBeenCalledWith(url, expect.objectContaining({
                method: 'POST',
                body: JSON.stringify(data),
            }));
        });

        it('should throw an error if the response is not ok', async () => {
            const url = 'https://api.example.com/data';
            const data = { key: 'value' };
            global.fetch = jest.fn().mockResolvedValue({
                ok: false,
            });

            await expect(httpClient.post(url, data)).rejects.toThrow('Network response was not ok');
        });
    });

    describe('delete', () => {
        it('should call fetch with the correct URL', async () => {
            const url = 'https://api.example.com/data';
            global.fetch = jest.fn().mockResolvedValue({
                ok: true,
                json: jest.fn().mockResolvedValue({}),
            });

            await httpClient.delete(url);

            expect(fetch).toHaveBeenCalledWith(url, expect.objectContaining({
                method: 'DELETE',
            }));
        });

        it('should throw an error if the response is not ok', async () => {
            const url = 'https://api.example.com/data';
            global.fetch = jest.fn().mockResolvedValue({
                ok: false,
            });

            await expect(httpClient.delete(url)).rejects.toThrow('Network response was not ok');
        });
    });
});