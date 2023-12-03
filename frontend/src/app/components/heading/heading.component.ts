import { Component } from '@angular/core';
import { Task } from '../../config.service';
import { HeadingService } from '../../heading.service';
import { Heading } from '../../heading';

@Component({
  selector: 'app-heading',
  templateUrl: './heading.component.html',
  styleUrls: ['./heading.component.css']
})
export class HeadingComponent {
  task: Task | undefined;

  title = 'frontend';

  constructor(private httpClientHeading: HeadingService) {}

  headings?: Heading[];

  ngOnInit(): void {
    this.httpClientHeading.getHeadings().subscribe(headings => {
      console.log(headings)
      this.headings = headings
    });
  }

  showTask() {
    // this.configService.
  }
}
