import { CookieStorage } from './CookieStorage';

describe('CookieStorage', () => {
    let cookieStorage: CookieStorage;

    beforeEach(() => {
        cookieStorage = new CookieStorage();
        document.cookie = ''; // Clear cookies before each test
    });

    test('setItem should save userName and password', () => {
        cookieStorage.setItem('userName', 'testUser');
        cookieStorage.setItem('password', 'testPassword');

        expect(cookieStorage.getItem('userName')).toBe('testUser');
        expect(cookieStorage.getItem('password')).toBe('testPassword');
    });

    test('getItem should return null for non-existing keys', () => {
        expect(cookieStorage.getItem('nonExistingKey')).toBeNull();
    });

    test('removeItem should delete the specified key', () => {
        cookieStorage.setItem('userName', 'testUser');
        cookieStorage.removeItem('userName');

        expect(cookieStorage.getItem('userName')).toBeNull();
    });
});