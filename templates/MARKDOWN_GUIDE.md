# Markdown Syntax Guide

This guide shows you how to use Markdown to format your documentation in Git repositories.

## Basic Formatting

### Headings

```markdown
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6
```

### Text Styling

```markdown
**Bold text**
*Italic text*
***Bold and italic text***
~~Strikethrough~~
```

**Bold text**
*Italic text*
***Bold and italic text***
~~Strikethrough~~

### Lists

#### Unordered Lists

```markdown
- Item 1
- Item 2
  - Subitem 2.1
  - Subitem 2.2
- Item 3
```

- Item 1
- Item 2
  - Subitem 2.1
  - Subitem 2.2
- Item 3

#### Ordered Lists

```markdown
1. First item
2. Second item
3. Third item
   1. Subitem 3.1
   2. Subitem 3.2
```

1. First item
2. Second item
3. Third item
   1. Subitem 3.1
   2. Subitem 3.2

### Links

```markdown
[Link text](https://www.example.com)
[Link with title](https://www.example.com "Link title")
```

[Link text](https://www.example.com)
[Link with title](https://www.example.com "Link title")

### Images

```markdown
![Alt text](image.jpg)
![Alt text with title](image.jpg "Image title")
```

## Code

### Inline Code

```markdown
Use `pinMode(13, OUTPUT)` to set pin 13 as output.
```

Use `pinMode(13, OUTPUT)` to set pin 13 as output.

### Code Blocks

````markdown
```
void setup() {
  pinMode(13, OUTPUT);
}

void loop() {
  digitalWrite(13, HIGH);
  delay(1000);
  digitalWrite(13, LOW);
  delay(1000);
}
```
````

```
void setup() {
  pinMode(13, OUTPUT);
}

void loop() {
  digitalWrite(13, HIGH);
  delay(1000);
  digitalWrite(13, LOW);
  delay(1000);
}
```

### Syntax Highlighting

````markdown
```arduino
void setup() {
  pinMode(13, OUTPUT);
}

void loop() {
  digitalWrite(13, HIGH);
  delay(1000);
  digitalWrite(13, LOW);
  delay(1000);
}
```
````

```arduino
void setup() {
  pinMode(13, OUTPUT);
}

void loop() {
  digitalWrite(13, HIGH);
  delay(1000);
  digitalWrite(13, LOW);
  delay(1000);
}
```

## Tables

```markdown
| Pin | Function      | Connected To |
|-----|---------------|--------------|
| 2   | Trigger Pin   | HC-SR04      |
| 3   | Echo Pin      | HC-SR04      |
| 10  | CS            | SD Card      |
| 11  | MOSI          | SD Card      |
| 12  | MISO          | SD Card      |
| 13  | SCK           | SD Card      |
```

| Pin | Function      | Connected To |
|-----|---------------|--------------|
| 2   | Trigger Pin   | HC-SR04      |
| 3   | Echo Pin      | HC-SR04      |
| 10  | CS            | SD Card      |
| 11  | MOSI          | SD Card      |
| 12  | MISO          | SD Card      |
| 13  | SCK           | SD Card      |

## Blockquotes

```markdown
> This is a blockquote
> 
> It can span multiple lines
```

> This is a blockquote
> 
> It can span multiple lines

## Horizontal Rules

```markdown
---
```

---

## Task Lists

```markdown
- [x] Task 1 (completed)
- [ ] Task 2 (not completed)
- [ ] Task 3 (not completed)
```

- [x] Task 1 (completed)
- [ ] Task 2 (not completed)
- [ ] Task 3 (not completed)

## Escaping Characters

```markdown
\*This text has asterisks\* but is not italic
```

\*This text has asterisks\* but is not italic

## Tips for Arduino Documentation

1. Use headings to organize your documentation:
   - # Project name
   - ## Hardware requirements
   - ## Wiring instructions
   - ## Code explanation

2. Create tables for pin connections:
   ```markdown
   | Arduino Pin | Component Pin | Description |
   |-------------|---------------|-------------|
   | 2           | Trigger       | HC-SR04     |
   | 3           | Echo          | HC-SR04     |
   ```

3. Use code blocks with arduino syntax highlighting for code examples:
   ````markdown
   ```arduino
   void setup() {
     // Your setup code
   }
   ```
   ````

4. Use images for circuit diagrams:
   ```markdown
   ![Circuit Diagram](circuit.jpg)
   ```

5. Create task lists for project steps:
   ```markdown
   - [x] Wire the circuit
   - [x] Upload the code
   - [ ] Test the sensor
   - [ ] Log data to SD card
   ``` 