import { animate, state, style, transition, trigger } from '@angular/animations';
import { Component } from '@angular/core';

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css'],
  animations: [
    trigger("chatBodyOpenClose", [
      state("open", style({
        height: "200px",
      })),
      state("close", style({
        height: "0px",
      })),
      transition('open <=> close', [
        animate('.3s'),
      ])
    ]),
  ]
})
export class ChatComponent {
  isOpen = false;

  toggle() {
    this.isOpen = !this.isOpen;
    // console.log(this.isOpen);
  }

  sendMessage(message: string) {
    if (message) { console.log("messag sent"); }
  }
}
