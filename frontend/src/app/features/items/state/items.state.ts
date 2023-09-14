import { Injectable } from "@angular/core";
import { BehaviorSubject } from "rxjs";

@Injectable({providedIn: "root"})
export class ItemsState {
    private currentItemId = new BehaviorSubject(0);

    public setCurrentItemId(id:number) {
        this.currentItemId.next(id);
    }

    public getCurrentItemId() {
        return this.currentItemId.asObservable();
    }

}