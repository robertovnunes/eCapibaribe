import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListItemsComponent } from './list-items.component';

// TODO: fix this test

describe('ListItemsComponent', () => {
    let component: ListItemsComponent;
    let fixture: ComponentFixture<ListItemsComponent>;

    beforeEach(() => {
        TestBed.configureTestingModule({
            declarations: [ListItemsComponent],
        });
        fixture = TestBed.createComponent(ListItemsComponent);
        component = fixture.componentInstance;
        fixture.detectChanges();
    });

    it('should create', () => {
        expect(component).toBeTruthy();
    });
});
