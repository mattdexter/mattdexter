#!/bin/env bash
psql -U postgres -c "create user $DB_USER password '$DB_PASS'"
psql -U postgres -c "create database $DB_NAME owner $DB_USER"