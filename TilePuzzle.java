import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.*;

public class TilePuzzle implements ActionListener {
    private TilePiece tiles[] = new TilePiece[12];
    private TilePiece blankTile = new TilePiece("blank_tile.jpg", 50, 50);

    TilePuzzle()
    {
        GridLayout layout = new GridLayout(3, 4);
        JFrame frame = new JFrame();
        JPanel panel = new JPanel(layout);

        for (int i = 0; i < tiles.length; i++) {
            TilePiece thisTile = new TilePiece(new String("tile_" + i + ".jpg"), 50, 50);
            tiles[i] = thisTile;
            panel.add(thisTile);
            thisTile.addActionListener(this);
        }

        panel.setSize(475, 400);

        frame.add(panel);
        frame.setVisible(true);
        frame.setSize(475, 400);
        frame.setTitle("Week 18 - Tile Puzzle");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    public void actionPerformed(ActionEvent e)
    {
        TilePiece t = (TilePiece) e.getSource();
        
    }
}