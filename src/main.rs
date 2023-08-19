mod entity;
mod item;

use std::io::{self, Write};

use rand::Rng;

#[derive(Default)]
struct Game {
    player: Player,
    boss: Boss,
}

fn boss_attack(player: &mut Player) {
    if rand::thread_rng().gen_ratio(2, 3) {
        player.reduce_health_by(10);
        println!("The dark lord attacks. It does 10 damage.");
    } else {
        println!("The dark lord attacks, but misses. You take no damage.");
    }
    println!("You have {} health remaining.", player.health);
}

fn use_ser(game: &mut Game) {
    if game.player.serum_count > 0 {
        game.player.serum_count -= 1;
    } else {
        println!("You are out of serum.");
    }
}

fn use_sser(game: &mut Game) {
    if game.player.super_serum_count > 0 {
        game.player.super_serum_count -= 1;
    } else {
        println!("You are out of super serum.");
    }
}

fn use_stam_fruit(game: &mut Game) {
    if game.player.stamina_fruit_count > 0 {
        game.player.stamina_fruit_count -= 1;
    } else {
        println!("You are out of stamina fruit.");
    }
}

fn fire_attack(game: &mut Game) {
    if game.player.fire_stamina > 0 {
        game.boss.health -= 15;
        game.player.fire_stamina -= 1;
        println!("You use a fire attack. It does 15 damage.");
    } else {
        println!("Your fire attack is out of stamina.");
    }
}

fn ice_attack(game: &mut Game) {
    if game.player.ice_stamina > 0 {
        game.boss.health -= 5;
        game.player.ice_stamina -= 1;
        println!("You use an ice attack. It does 5 damage and freezes the dark lord.");
    } else {
        println!("Your ice attack is out of stamina.");
    }
    game.boss.frozen = true;
}

fn earth_attack(game: &mut Game) {
    if game.player.earth_stamina > 0 {
        game.boss.health -= 5;
        game.player.health += 5;
        game.player.earth_stamina -= 1;
        println!("You use an earth attack. It does 5 damage and you heal 5 health.");
    } else {
        println!("Your earth attack is out of stamina.");
    }
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
            }
        } else if action.to_lowercase() == "flee" {
            input("You surrender the battle. Press any key to quit.");
            running = false;
        } else {
            println!("Please input a valid action next time. You forfeit your turn.");
        }

        if game.boss.frozen {
            game.boss.frozen = false;
        } else {
            boss_attack(&mut game.player);
        }

        if !game.player.is_alive() {
            println!("\nYou have died.");
            running = false;
        } else if !game.boss.is_alive() {
            println!("Congratulations! You defeated the boss!");
            running = false;
        }
    }
}
