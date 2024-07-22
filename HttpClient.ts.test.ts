describe('HttpClient', () => {
    let httpClient: IHttpClient;

    beforeEach(() => {
        httpClient = new HttpClient();
    });

    it('should fetch data with GET method', async () => {
        const mockResponse = { data: 'test' };
        global.fetch = jest.fn().mockResolvedValue({
            ok: true,
            json: jest.fn().mockResolvedValue(mockResponse),
        });

        const result = await httpClient.get('/test-url');
        expect(result).toEqual(mockResponse);
        expect(fetch).toHaveBeenCalledWith('/test-url');
    });

    it('should post data with POST method', async () => {
        const mockResponse = { success: true };
        const dataToPost = { name: 'test' };
        global.fetch = jest.fn().mockResolvedValue({
            ok: true,
            json: jest.fn().mockResolvedValue(mockResponse),
        });

        const result = await httpClient.post('/test-url', dataToPost);
        expect(result).toEqual(mockResponse);
        expect(fetch).toHaveBeenCalledWith('/test-url', expect.objectContaining({
            method: 'POST',
            body: JSON.stringify(dataToPost),
        }));
    });

    it('should delete data with DELETE method', async () => {
        const mockResponse = { success: true };
        global.fetch = jest.fn().mockResolvedValue({
            ok: true,
            json: jest.fn().mockResolvedValue(mockResponse),
        });

        const result = await httpClient.delete('/test-url');
        expect(result).toEqual(mockResponse);
        expect(fetch).toHaveBeenCalledWith('/test-url', expect.objectContaining({
            method: 'DELETE',
        }));
    });

    it('should throw an error on GET failure', async () => {
        global.fetch = jest.fn().mockResolvedValue({
            ok: false,
        });

        await expect(httpClient.get('/test-url')).rejects.toThrow('Network response was not ok');
    });

    it('should throw an error on POST failure', async () => {
        global.fetch = jest.fn().mockResolvedValue({
            ok: false,
        });

        await expect(httpClient.post('/test-url', {})).rejects.toThrow('Network response was not ok');
    });

    it('should throw an error on DELETE failure', async () => {
        global.fetch = jest.fn().mockResolvedValue({
            ok: false,
        });

        await expect(httpClient.delete('/test-url')).rejects.toThrow('Network response was not ok');
    });
});