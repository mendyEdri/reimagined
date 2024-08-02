export interface IStorage {
    setItem(key: string, value: string): void;
    getItem(key: string): string | null;
    removeItem(key: string): void;
}

export class CookieStorage implements IStorage {
    setItem(key: string, value: string): void {
        document.cookie = `${key}=${value}; path=/`;
    }

    getItem(key: string): string | null {
        const name = `${key}=`;
        const decodedCookie = decodeURIComponent(document.cookie);
        const cookieArray = decodedCookie.split(';');
        for (let i = 0; i < cookieArray.length; i++) {
            let cookie = cookieArray[i].trim();
            if (cookie.indexOf(name) === 0) {
                return cookie.substring(name.length, cookie.length);
            }
        }
        return null;
    }

    removeItem(key: string): void {
        document.cookie = `${key}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;`;
    }
}