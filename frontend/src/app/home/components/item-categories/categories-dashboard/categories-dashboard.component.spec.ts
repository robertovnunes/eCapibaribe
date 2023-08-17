import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CategoriesDashboardComponent } from './categories-dashboard.component';

describe('CategoriesDashboardComponent', () => {
  let component: CategoriesDashboardComponent;
  let fixture: ComponentFixture<CategoriesDashboardComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CategoriesDashboardComponent]
    });
    fixture = TestBed.createComponent(CategoriesDashboardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
