import { IFirebaseClient } from './IFirebaseClient';

/**
 * Generic Firebase Client for getting and updating data.
 * This client uses methods to interact with Firebase services for data retrieval and updates.
 */
export class FirebaseClient<T> implements IFirebaseClient<T> {
    private db: any; // Assume this is your Firebase database instance

    constructor(db: any) {
        this.db = db;
    }

    async getData(id: string): Promise<T> {
        const snapshot = await this.db.collection('USERS_LIVE_SITES').doc(id).get();
        return snapshot.data() as T;
    }

    async updateData(id: string, data: T): Promise<void> {
        await this.db.collection('USERS_LIVE_SITES').doc(id).update(data);
    }
}