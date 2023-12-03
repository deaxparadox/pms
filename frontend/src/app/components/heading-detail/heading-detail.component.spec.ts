import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HeadingDetailComponent } from './heading-detail.component';

describe('HeadingDetailComponent', () => {
  let component: HeadingDetailComponent;
  let fixture: ComponentFixture<HeadingDetailComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [HeadingDetailComponent]
    });
    fixture = TestBed.createComponent(HeadingDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
