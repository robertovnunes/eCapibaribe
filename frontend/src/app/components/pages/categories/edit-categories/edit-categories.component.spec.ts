import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditCategoriesComponent } from './edit-categories.component';

describe('EditCategoriesComponent', () => {
  let component: EditCategoriesComponent;
  let fixture: ComponentFixture<EditCategoriesComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [EditCategoriesComponent]
    });
    fixture = TestBed.createComponent(EditCategoriesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
