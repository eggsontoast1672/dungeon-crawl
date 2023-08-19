use std::{
    io::{self, Write},
    process,
};

use rand::Rng;

struct Game {
    boss_health: usize,
    player_health: usize,
    fire_stam: usize,
    ice_stam: usize,
    earth_stam: usize,
    ser_num: usize,
    sser_num: usize,
    stam_fruit: usize,
}

impl Default for Game {
    fn default() -> Self {
        Self {
            boss_health: 100,
            player_health: 20,
            fire_stam: 5,
            ice_stam: 5,
            earth_stam: 5,
            ser_num: 3,
            sser_num: 2,
            stam_fruit: 1,
        }
    }
}

fn boss_attack(game: &mut Game) {
    let num = rand::thread_rng().gen_range(0..=2);
    if num == 0 {
        println!("The dark lord attacks, but misses. You take no damage.");
        println!("You have {} health remaining.", game.player_health);
    } else {
        game.player_health -= 10;
        println!("The dark lord attacks. It does 10 damage.");
        println!("You have {} health remaining.", game.player_health);
    }
}

fn check_health(game: &Game) {
    if game.player_health <= 0 {
        println!("\nYou have died.");
        input("Press any button to quit.");
        process::exit(0);
    }
    if game.boss_health <= 0 {
        println!("Congratulations! You defeated the boss!");
        input("Press any button to quit.");
        process::exit(0);
    }
}

fn use_ser(game: &mut Game) {
    if game.ser_num > 0 {
        game.ser_num -= 1;
    } else {
        println!("You are out of serum.");
    }
    boss_attack(game);
    check_health(game);
}

fn use_sser(game: &mut Game) {
    if game.sser_num > 0 {
        game.sser_num -= 1;
    } else {
        println!("You are out of super serum.");
    }
    boss_attack(game);
    check_health(game);
}

fn use_stam_fruit(game: &mut Game) {
    if game.stam_fruit > 0 {
        game.stam_fruit -= 1;
    } else {
        println!("You are out of stamina fruit.");
    }
    boss_attack(game);
    check_health(game);
}

fn fire_attack(game: &mut Game) {
    if game.fire_stam > 0 {
        game.boss_health -= 15;
        game.fire_stam -= 1;
        println!("You use a fire attack. It does 15 damage.");
    } else {
        println!("Your fire attack is out of stamina.");
    }
    boss_attack(game);
    check_health(game);
}

fn ice_attack(game: &mut Game) {
    if game.ice_stam > 0 {
        game.boss_health -= 5;
        game.ice_stam -= 1;
        println!("You use an ice attack. It does 5 damage and freezes the dark lord.");
    } else {
        println!("Your ice attack is out of stamina.");
    }
}

fn earth_attack(game: &mut Game) {
    if game.earth_stam > 0 {
        game.boss_health -= 5;
        game.player_health += 5;
        game.earth_stam -= 1;
        println!("You use an earth attack. It does 5 damage and you heal 5 health.");
    } else {
        println!("Your earth attack is out of stamina.");
    }
    boss_attack(game);
    check_health(game);
}

fn input(prompt: &str) -> String {
    print!("{}", prompt);
    io::stdout().flush().unwrap();
    io::stdin().lines().next().unwrap().unwrap()
}

fn main() {
    println!("You face off against the dark lord.");

    let mut running = true;
    let mut game = Game::default();
    while running {
        let action = input("\nWhat would you like to do? (Attack, Item, Flee): ");
        if action.to_lowercase() == "attack" {
            let attack = input("What attack do you want to use? (Fire, Ice, Earth): ");
            if attack.to_lowercase() == "fire" {
                fire_attack(&mut game);
            } else if attack.to_lowercase() == "ice" {
                ice_attack(&mut game);
            } else if attack.to_lowercase() == "earth" {
                earth_attack(&mut game);
            } else {
                println!("Please input a valid attack next time. You forfeit your turn.");
                boss_attack(&mut game);
                check_health(&mut game);
            }
        } else if action.to_lowercase() == "item" {
            let item = input("What item do you want to use? (Serum, Super Serum, Stamina Fruit): ");
            if item.to_lowercase() == "serum" {
                use_ser(&mut game);
            } else if item.to_lowercase() == "super serum" {
                use_sser(&mut game);
            } else if item.to_lowercase() == "stamina fruit" {
                use_stam_fruit(&mut game);
            } else {
                println!("Please input a valid item next time. You forfeit your turn.");
                boss_attack(&mut game);
                check_health(&game);
            }
        } else if action.to_lowercase() == "flee" {
            input("You surrender the battle. Press any key to quit.");
            running = false;
        } else {
            println!("Please input a valid action next time. You forfeit your turn.");
            boss_attack(&mut game);
            check_health(&game);
        }
    }
}
