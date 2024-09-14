use std::fs;

fn main() {
    let n: usize = fs::read_to_string("input.txt").unwrap().trim().parse().unwrap();

    let mut output = String::new();
    for i in 0..n {
        output.push_str(&format!("{:width$}{}\n", "", "*".repeat(2 * i + 1), width = n - i - 1));
    }
    for i in (0..n - 1).rev() {
        output.push_str(&format!("{:width$}{}\n", "", "*".repeat(2 * i + 1), width = n - i - 1));
    }

    fs::write("output.txt", output).expect("Unable to write file");
}
