import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ItemCategoriesComponent } from './item-categories.component';

describe('ItemCategoriesComponent', () => {
  let component: ItemCategoriesComponent;
  let fixture: ComponentFixture<ItemCategoriesComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ItemCategoriesComponent]
    });
    fixture = TestBed.createComponent(ItemCategoriesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
