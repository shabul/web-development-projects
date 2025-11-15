# KBC Game - PHP Quiz Application

A web-based quiz game inspired by "Kaun Banega Crorepati" (KBC), built with PHP, HTML, CSS, and JavaScript. Features multiple levels, lifelines, and an engaging user interface.

## Features

- **Multiple Levels**: Progressive difficulty with 9+ question levels
- **Lifelines**: Classic KBC lifelines (50:50, Phone a Friend, Ask the Audience)
- **Interactive UI**: Engaging interface with sound effects and animations
- **Money Ladder**: Progressive prize money system
- **Question Bank**: Diverse set of questions across various topics
- **Responsive Design**: Works on desktop and mobile devices
- **Audio Integration**: Background music and sound effects

## Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: PHP
- **Audio**: MP3 audio integration
- **Styling**: Custom CSS with animations

## Requirements

- Web server (Apache/Nginx)
- PHP 7.0+
- Modern web browser with JavaScript enabled
- Audio support for sound effects

## Installation

1. **Setup Web Server**
   - Install XAMPP/WAMP/LAMP or use any web server
   - Start Apache service

2. **Deploy Application**
   - Copy the `kbc-game-php` folder to your web server directory
   - For XAMPP: Place in `htdocs/kbc-game-php/`

3. **Access the Game**
   - Open browser and navigate to `http://localhost/kbc-game-php/`
   - Start playing immediately (no database setup required)

## Project Structure

```
kbc-game-php/
├── levels/                # Game levels
│   ├── level1/           # Level 1 questions and logic
│   ├── level2/           # Level 2 questions and logic
│   ├── level3/           # Level 3 questions and logic
│   └── level9/           # Level 9 questions and logic
├── assets/               # Game assets
│   ├── kbc.jpg          # Game background image
│   ├── pic.jpeg         # Additional images
│   ├── swayamvaram.mp3  # Background music
│   ├── qstns.txt        # Question bank
│   └── bluprint.txt     # Game blueprint
└── README.md            # This file
```

## Game Flow

### Level Structure
Each level contains:
- `index.php` - Level entry point
- `page1.html` to `page7.html` - Question pages
- `money1.html` to `money6.html` - Money ladder displays
- `lifeline.html` - Lifeline options
- `fire.html` - Wrong answer page
- `cong.html` - Congratulations page

### Game Progression
1. **Start Game**: Begin with Level 1
2. **Answer Questions**: Progress through multiple-choice questions
3. **Use Lifelines**: Access help when needed
4. **Win Money**: Earn virtual prize money for correct answers
5. **Complete Levels**: Advance to higher difficulty levels

## Lifelines Available

### 1. 50:50
- Removes two incorrect options
- Leaves one correct and one incorrect answer
- Can be used once per game

### 2. Phone a Friend
- Simulated friend assistance
- Provides hint or suggestion
- Limited time feature

### 3. Ask the Audience
- Shows audience poll results
- Displays percentage breakdown
- Visual representation of popular choice

## Game Features

### Question System
- Multiple-choice questions (A, B, C, D)
- Progressive difficulty across levels
- Diverse topics and categories
- Timed responses (optional)

### Money Ladder
- ₹1,000 to ₹1 Crore progression
- Safe points at certain levels
- Risk/reward decision making

### Audio Experience
- Background music during gameplay
- Sound effects for correct/incorrect answers
- Tension-building audio cues
- Celebration sounds for wins

## Customization

### Adding New Questions
1. Edit question files in each level directory
2. Update `qstns.txt` in assets folder
3. Modify HTML pages with new questions
4. Ensure proper answer validation

### Modifying Levels
1. Create new level directories
2. Copy structure from existing levels
3. Update question content and difficulty
4. Link levels in navigation flow

### Styling Changes
1. Modify CSS in individual HTML files
2. Update background images and colors
3. Customize fonts and animations
4. Adjust responsive design elements

## File Descriptions

### Core Files
- `index.php` - Game launcher and main entry point
- `sample.html` - Template for question pages
- Various `page*.html` - Individual question screens
- `money*.html` - Prize money display screens

### Asset Files
- `kbc.jpg` - Main game background
- `pic.jpeg` - Additional visual elements
- `swayamvaram.mp3` - Background music track
- Audio files for sound effects

### Configuration Files
- `qstns.txt` - Question database
- `bluprint.txt` - Game structure blueprint

## Browser Compatibility

- **Chrome**: Fully supported
- **Firefox**: Fully supported
- **Safari**: Supported with minor limitations
- **Edge**: Supported
- **Mobile Browsers**: Responsive design included

## Performance Optimization

- Optimized images for web
- Compressed audio files
- Minimal JavaScript for smooth gameplay
- Efficient CSS for quick loading

## Troubleshooting

### Common Issues

1. **Audio Not Playing**
   - Check browser audio permissions
   - Ensure MP3 codec support
   - Verify file paths are correct

2. **Images Not Loading**
   - Check file permissions
   - Verify image file paths
   - Ensure web server is running

3. **Navigation Issues**
   - Check PHP configuration
   - Verify all HTML files are present
   - Test JavaScript functionality

### Performance Issues
- Clear browser cache
- Check server resources
- Optimize image sizes
- Minimize HTTP requests

## Educational Use

This game can be used for:
- **Learning**: Educational quiz content
- **Training**: Corporate training programs
- **Entertainment**: Family game nights
- **Assessment**: Knowledge testing

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Add new questions or improve gameplay
4. Test thoroughly across different browsers
5. Submit a pull request

## Future Enhancements

- **Database Integration**: Store questions and scores
- **User Accounts**: Player registration and progress tracking
- **Leaderboards**: High score tracking
- **More Lifelines**: Additional help options
- **Mobile App**: Native mobile application
- **Multiplayer Mode**: Compete with friends
- **Custom Themes**: Different visual themes
- **Question Categories**: Subject-specific quizzes

## License

This project is for educational and entertainment purposes. Feel free to modify and distribute according to your needs.

## Credits

- Inspired by the popular TV show "Kaun Banega Crorepati"
- Audio and visual assets used for educational purposes
- Game mechanics based on classic quiz show format

## Support

For questions, issues, or contributions:
1. Create an issue in this repository
2. Check existing documentation
3. Test the game thoroughly before reporting bugs

Enjoy playing the KBC Game! 🎮🏆
